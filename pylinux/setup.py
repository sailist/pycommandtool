from setuptools import setup, find_packages

setup(
    name='pylinux',
    version='0.0.1.1.dev1',
    description='convert markdown 2 latex code perfactly,support Chinese Language',
    url='https://github.com/sailist/pycommandtool/tree/master/pylinux',
    author='sailist',
    author_email='sailist@outlook.com',
    license='MIT',
    include_package_data=True,
    install_requires=[
        # "colorprint",
    ],
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
    keywords='win linux command',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'head = pylinux.txteditor.head:main',
            'tail = pylinux.txteditor.tail:main',
            'egrep = pylinux.txteditor.egrep:main',
            'wc = pylinux.txteditor.wc:main',
            'ls = pylinux.diskmanager.ls:main',
            'tee = pylinux.manager.tee:main',
        ]
    },
)