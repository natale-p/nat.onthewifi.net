#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nat'
SITENAME = 'Nat On The Wifi - My Personal Page'
SITEURL = ''
THEME = 'm.css/pelican-theme'
PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

PAGES_SORT_ATTRIBUTE = 'sortorder'

HEADERIMAGE = "header.png"

EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/header.png' : {'path': 'images/header.png'}
}


THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css', '/static/resume.css']
M_THEME_COLOR = '#22272e'
M_FAVICON = ('favicon.ico', 'image/x-ico')
M_SITE_LOGO = 'images/header.png'

M_LINKS_NAVBAR1 = [('Welcome', 'index.html', 'welcome', []),
                   ('Blog',    'author/nat.html', '[blog]', []),
                   ('Papers',  'pages/papers.html', 'papers', []),
                   ('Resume',  'pages/resume.html', 'resume', [])]

M_NEWS_ON_INDEX = ("Latest entries", 3)

PLUGIN_PATHS = ['m.css/plugins/m', 'm.css/plugins', 'm.css/pelican-plugins']
PLUGINS = ['htmlsanity']

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widgets
#SOCIAL = (
#    ('github', 'https://github.com/natale-p'),
#    ('linkedin', 'https://www.linkedin.com/in/natalep'),
#)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#Profile information
R_NAME = 'Natale Patriciello'
R_DESC = 'Computer scientist'
R_MAIL = 'npatriciello@acm.org'

R_LINKEDIN = 'linkedin.com/in/natale-p'
R_SKYPE = 'natale.patriciello'

R_TOT_PAPERS = '41'
R_CITATIONS = '549'
R_H_INDEX = '13'

R_LANGUAGES = [
    {
        'name': 'Italian',
        'level': 5,
        'black': 0
    },
    {
        'name': 'English',
        'level': 5,
        'black': 0
    },
    {
        'name': 'Spanish',
        'level': 5,
        'black': 0
    }
]

R_PROGRAMMING = [
    {
        'name': 'C/C++',
        'level': 5,
        'black': 0
    },
    {
        'name': 'Python',
        'level': 5,
        'black': 0
    },
    {
        'name': 'Protocols',
        'level': 5,
        'black': 0
    },
    {
        'name': 'SW Design',
        'level': 5,
        'black': 0
    },
    {
        'name': 'AWS Cloud',
        'level': 4,
        'black': 1
    },
    {
        'name': 'K8S',
        'level': 4,
        'black': 1
    },
]

R_EDUCATION = [
    {
        'date': '2014-2016',
        'title': 'Ph.D. in ICT',
        'where': 'DIEF, University of Modena (Italy)',
        'what': 'Avoiding Congestion in Emergency Networks'
    },
    {
        'date': '2010-2013',
        'title': 'M.Sc. magna cum laude',
        'where': 'CS, University of Bologna (Italy)',
        'what': 'Majoring in Theoretical Computer Science: A prototype for deadlock analysis'
    },
    {
        'date': '2007-2010',
        'title': 'B.Sc.',
        'where': 'FIM, University of Modena (Italy)',
        'what': 'Majoring in Computer Science'
    }
]

R_JOBS = [
    {
        'job_title': 'Senior Software Engineer',
        'date': '07/2022 - until now',
        'company': 'Vonage, Barcelona (Spain)',
        'details': 'Media Routing supervision and guidance for a WebRTC-based backend.<ul><li>Leading a team of five people</li><li>Faciliting cross-functional team communication</li></ul>'
    },
    {
        'job_title': 'Software Media Engineer',
        'date': '12/2020 - 07/2022',
        'company': 'Vonage, Barcelona (Spain)',
        'details': 'Rate control research and implementation for a WebRTC-based backend.<ul><li>On-time feature delivery with proper ticket management</li><li>Identified and resolved critical bugs in the production codebase</li><li>Proactively maintained code quality through active participation in code assessments and reviews.</li></ul>'
    },
    {
        'job_title': 'Researcher',
        'date': '10/2017 - 11/2020',
        'company': 'CTTC, Barcelona (Spain)',
        'details': '5G NR/NR-U design and implementation in mmWave bands.<ul><li>Presented various papers and posters in international conferences</li><li>Offline and online interactions for maintaining an open-source simulator</li></ul>'
    },
    {
        'job_title': 'Scientific Software Developer',
        'date': '03/2017 - 10/2017',
        'company': 'TSS, Barcelona (Spain)',
        'details': 'V2X Framework development inside Aimsun Simulator'
    },
    {
        'job_title': 'Indepentent Contractor',
        'date': '02/2017 - 05/2017',
        'company': 'NITEL, Roma (Italy)',
        'details': 'TCP Wave - TCP congestion control implementation in the Linux kernel'
    },
    {
        'job_title': 'Researcher',
        'date': '04/2013 - 12/2016',
        'company': 'University of Modena (Italy)',
        'details': 'European FP7, "PPDR-TC (FP7 313015)" <br> Italian PRIN, "SFINGI: SoFtware-routers to Improve Next Generation Internet"'
    },
]

R_AWARDS = [
    {
        'award_title': 'Mentor for Google Summer of Code (GSoC)',
        'date': '2018 - 2019',
        'details' : '5G/NR projects integration in ns-3',
    },
    {
        'award_title': 'Best paper award at ISNCC 2018',
        'date': '2018',
        'details' : 'Paper title: TCP Wave estimation of the optimal operating point using ACK trains',
    },
    {

        'award_title': 'Student for Google Summer of Code (GSoC)',
        'date': '2015',
        'details' : 'ns-3 TCP layer refactoring with validation and automated test',
    },
    {

        'award_title': 'ESA Summer of Code in Space (SOCIS)',
        'date': '2014',
        'details' : 'ns-3 TCP variants for satellite communications',
    },
]


PIC = 'profile.png'

