"""\
This is the game "Under the Xadian Sky", based on the Netflix series "The Dragon Prince".
Copyright (C) 2020 Vo Thuong

Current version: Unreleased

Dependencies: (default modules installed with python are not listed)
pygame 2.0.0.dev8
logzero
pydraw.py
tilemap.py

Thank you kenney, for making this possible.\
"""

"""
Current debug version progress:
 * TODO Entry screen: (Play, Options, Help)
 * Intro screen progress: 100%
    * Save file buttons: Complete
    * Save checking: Complete
    * Name entry: Complete
    * Choosing avatar: Complete
 * TODO Main game progress: 0%
"""

import source

source.intro.start()
source.main.start()