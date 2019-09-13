Install
-------

Install system requirements for ``lxml``

::

    % sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev zlib1g-dev

    or

    % brew install libxml2

Install with ``pip``

::

    % pip3 install parse-helper

    Optionally install ipython with ``pip3 install ipython`` to enable
    ``ph-soup-explore`` command

Usage
-----

The ``ph-ddg``, ``ph-download-files``, ``ph-download-file-as``, and
``ph-soup-explore`` scripts are provided

::

    $ venv/bin/ph-ddg --help
    Usage: ph-ddg [OPTIONS] [QUERY]

      Pass a search query to duckduckgo api

    Options:
      --help  Show this message and exit.

    $ venv/bin/ph-download-files --help
    Usage: ph-download-files [OPTIONS] [ARGS]...

      Download all links to local files

      - args: urls or filenames containing urls

    Options:
      --help  Show this message and exit.

    $ venv/bin/ph-download-file-as --help
    Usage: ph-download-file-as [OPTIONS] URL [LOCALFILE]

      Download link to local file

      - url: a string - localfile: a string

    Options:
      --help  Show this message and exit.

    $ venv/bin/ph-soup-explore --help
    Usage: ph-soup-explore [OPTIONS] [URL_OR_FILE]

      Create a soup object from a url or file and explore with ipython

    Options:
      --help  Show this message and exit.

.. code:: python

    In [1]: import parse_helper as ph

    In [2]: ph.USER_AGENT
    Out[2]: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36'

    In [3]: ph.duckduckgo_api('adventure time')
    2019-08-27 06:21:05,303: Fetching JSON from https://api.duckduckgo.com?q=adventure+time&format=json
    Out[3]:
    [{'text': 'Adventure Time An American animated television series created by Pendleton Ward for Cartoon Network.',
      'thumbnail': 'https://duckduckgo.com/i/fb8f17fd.png',
      'link': 'https://duckduckgo.com/Adventure_Time'},
     {'text': '"Adventure Time" (pilot) An animated short created by Pendleton Ward, as well as the pilot to the Cartoon Network series...',
      'thumbnail': 'https://duckduckgo.com/i/aa9b49e0.png',
      'link': 'https://duckduckgo.com/Adventure_Time_(pilot)'},
     {'text': "Adventure Time (1959 TV series) A local children's television show on WTAE-TV 4 in Pittsburgh, Pennsylvania, from 1959 to 1975.",
      'thumbnail': '',
      'link': 'https://duckduckgo.com/Adventure_Time_(1959_TV_series)'},
     {'text': "Adventure Time (1967 TV series) A Canadian children's adventure television series which aired on CBC Television in 1967 and 1968.",
      'thumbnail': '',
      'link': 'https://duckduckgo.com/Adventure_Time_(1967_TV_series)'},
     {'text': 'Adventure Time (album) The second album for the rock/pop trio The Elvis Brothers.',
      'thumbnail': '',
      'link': 'https://duckduckgo.com/Adventure_Time_(album)'}]
