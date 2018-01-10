import setuptools

setuptools.setup(
    name="MeetSMS",
    version="1.1",
    url="https://github.com/unique1o1/Meet-SMS",

    author="Yunik Maharjan",
    author_email="yunik.maharjan@icloud.com",
    license='MIT',
    description="Send SMS easily from MeetSMS",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['requests'],
    platform=['unix'],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
    ],
    download_url='https://github.com/unique1o1/Meet-SMS/archive/v1.3.1.tar.gz',
    entry_points="""
    [console_scripts]
    sms=meetsms.meetsms:main
    """,
)
