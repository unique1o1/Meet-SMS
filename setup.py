import setuptools

setuptools.setup(
    name="SimpleSMS",
    version="1.1",
    url="https://github.com/unique1o1/SimpleSMS",

    author="Yunik Maharjan",
    author_email="yunik.maharjan@icloud.com",

    description="Send SMS easily from MeetSMS",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=[requests],

    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
    ],
    entry_points="""
    [console_scripts]
    sms=SimepleSMS.meetsms
    """,
)
