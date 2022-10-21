#!/usr/bin/env python3
# coding: utf-8
# Copyright (C) 2022, [Breezedeus](https://github.com/breezedeus).

import os
from setuptools import find_packages, setup
from pathlib import Path

PACKAGE_NAME = "pix2text"

here = Path(__file__).parent

long_description = (here / "README.md").read_text(encoding="utf-8")

about = {}
exec(
    (here / PACKAGE_NAME.replace('.', os.path.sep) / "__version__.py").read_text(
        encoding="utf-8"
    ),
    about,
)

required = [
    "click",
    "tqdm",
    "cnstd>=1.2.1",
    "cnocr>=2.2.2",
    "pix2tex",
]
extras_require = {
    "dev": ["pip-tools", "pytest"],
    "serve": ["uvicorn[standard]", "fastapi", "python-multipart", "pydantic"],
}

entry_points = """
[console_scripts]
p2t = pix2text.cli:cli
"""

setup(
    name=PACKAGE_NAME,
    version=about['__version__'],
    description="Python3 package to extract text information from images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='breezedeus',
    author_email='breezedeus@163.com',
    license='MIT',
    url='https://github.com/breezedeus/pix2text',
    platforms=["Mac", "Linux", "Windows"],
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        (
            '',
            [
                'pix2text/latex_config.yaml',
            ],
        )
    ],
    entry_points=entry_points,
    install_requires=required,
    extras_require=extras_require,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
