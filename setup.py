from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

test_deps: [] = [
]

setup(
    name="click_demo",
    version="0.0.1",
    author="Rakesh Bute",
    author_email="rakeshbute@gmail.com",
    description="Test setup for learning click features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rbute/click_demo",
    project_urls={
        "Code": "https://github.com/rbute/click_demo",
        # "Issue tracker": "https://github.com/rbute/click_demo/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.6',
    tests_require=test_deps,
    install_requires=
    [
        'click>=7.0',
    ],
    entry_points={
        'console_scripts': [
            'demo_cli=click_demo.loader:cli',
        ],
        'click_demo_plugins': [
            'cdp=click_demo.plugin:click_demo_plugin_main',
        ]
    }
)
