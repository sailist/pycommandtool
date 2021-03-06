from setuptools import setup,find_packages

setup(
    name='quickfile',
    version='0.2.4.10.dev1',
    description='quick build templete file',
    url='https://github.com/sailist/pycommandtool/tree/master/pylinux',
    author='sailist',
    author_email='sailist@outlook.com',
    license='MIT',
    include_package_data = True,
    # install_requires = [],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='quick build files',
    packages=find_packages(),
    package_data = {
        "":["*.cmd","*.md"]
    },
    entry_points={
        'console_scripts':[
            'quickf = quickfile.quickfile:main',
            'qcrf = quickfile.quickfile:main'
        ]
      },
)