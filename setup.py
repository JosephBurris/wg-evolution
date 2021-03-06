#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Valerio Cosentino <valcos@bitergia.com>
#


from setuptools import setup


setup(name="wg-evolution-implementations",
      version="0.0.1",
      install_requires=[
        'perceval>=0.12.18',
        'pandas>=0.1.9',
        'fpdf>=1.7.2',
        'matplotlib>=2.2.4'
      ],
      setup_requires=[
          'wheel'
      ],
      packages=[
          'implementations'
      ],
      scripts=[
          'bin/analyze'
      ],
      zip_safe=False)
