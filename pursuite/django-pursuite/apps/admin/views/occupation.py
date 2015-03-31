# -*- coding: utf-8 -*-
"""
    admin.views.occupation

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
import os
from collections import defaultdict, OrderedDict, Counter

from jinja2 import Environment, FileSystemLoader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from admin.models.occupation import Occupation
from admin.models.qualification_pack import QualificationPack
from django.template import RequestContext
from django.shortcuts import render_to_response


def _get_rendering_settings(context):
    """
    Return the rendering settings
    """
    rv = {
        'ROW_HEIGHT': 100,          # Height of each row
        'LEGEND_WIDTH': 100,        # Width of the right side legend
        'TRACKS_AREA_WIDTH': 800,   # Width of the main tracks area
    }

    # Compute the other settings based on above values
    rv['TRACK_WIDTH'] = rv['TRACKS_AREA_WIDTH'] / context['total_tracks']

    # Total height of the image is the total row height + the height of
    # the heading and track name bottom row (n + 2)
    rv['SVG_HEIGHT'] = (context['total_levels'] + 2) * rv['ROW_HEIGHT']
    rv['SVG_WIDTH'] = rv['TRACKS_AREA_WIDTH'] + rv['LEGEND_WIDTH']

    rv['BUBBLE_HEIGHT'] = rv['ROW_HEIGHT'] * 0.8
    return rv


def view_career_map(request, slug):
    """
    Returns an SVG image of the career map for the given occupation
    """
    occupation = get_object_or_404(Occupation, slug=slug)

    level_data = defaultdict(dict)

    # A set of tracks in this career map
    tracks = {}

    # A pretty large set of colors to choose from
    colors = [
        'Blue',
        'BlueViolet',
        'Brown',
        'Yellow',
        'Coral',
        'Orange',
        'ForestGreen',
        'Gold',
        'Indigo',
        'LightSeaGreen ',
        'Maroon',
        'Purple',
    ]

    for track in occupation.tracks.all():
        tracks.setdefault(track, colors.pop())

        for qp in track.qualification_packs:
            level_data[qp.level].setdefault(track, set()).add(qp)

    level_counter = Counter()
    for level in level_data.keys():
        level_counter[
            QualificationPack.get_major_level(level)
        ] += 1

    context = {
        'occupation': occupation,

        'level_data': level_data,
        'total_levels': len(level_data.keys()),
        'level_counter': level_counter,

        'tracks': OrderedDict(
            sorted(tracks.items(), key=lambda item: item[0].id)
        ),
        'total_tracks': len(tracks.keys()) or 1,    # Avoid 0 tracks

        'level_names': {
            'el': 'Entry Level',
            'ml': 'Middle Level',
            'll': 'Leadership Level',
        },
    }

    # Update the context with the SVG rendering settings
    context.update(_get_rendering_settings(context))

    directory = os.path.abspath(os.path.dirname(__file__))
    env = Environment(
        loader=FileSystemLoader(directory),
        autoescape=True,
        extensions=[
            'jinja2.ext.autoescape',
            'jinja2.ext.loopcontrols',
            'jinja2.ext.with_',
        ],
    )

    template = env.get_template('career_map.svg')
    return HttpResponse(
        template.render(context),
        content_type='image/svg+xml'
    )


def render(request, slug):
    """
        Render occupation
    """
    occupation = get_object_or_404(Occupation, slug=slug)

    return render_to_response(
        'admin/occupation.html',
        {'occupation': occupation},
        context_instance=RequestContext(request),
    )
