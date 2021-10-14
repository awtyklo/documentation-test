extensions = ['myst_parser']
html_theme = 'sphinx_material'
html_title = 'Documentation'
html_sidebars = { '**': ['globaltoc.html', 'localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }
html_theme_options = {
    'nav_title': 'SMART EMS',
    'color_primary': 'blue',
    'globaltoc_depth': 1,
    'globaltoc_collapse': False,
    'version_dropdown': True,
    'version_info': {
        'development': 'development',
        'stable': '',
        'v2.0.0': 'v2.0.0',
        'v2.1.0': 'v2.1.0',
        'v2.1.5': 'v2.1.5',
        'v2.4.0': 'v2.4.0',
    },
}