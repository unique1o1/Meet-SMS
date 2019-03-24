import setuptools

setuptools.setup(
    name="MeetSMS",
    version="1.3.3",
    url="https://github.com/unique1o1/Meet-SMS",

    author="Yunik Maharjan",
    author_email="yunik.maharjan@icloud.com",
    license='MIT',
    description="Send SMS easily using MeetSMS",
    long_description=open('README.md').read(),
    download_url="https://github.com/unique1o1/Meet-SMS/archive/v1.3.2.tar.gz",
    packages=setuptools.find_packages(),

    install_requires=['requests'],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points="""
    [console_scripts]
    sms=meetsms.meetsms:main
    """,
)
