from setuptools import setup, find_packages

setup(
    name='pylinux',
    version='0.6.0.1.dev1',
    description='convert markdown 2 latex code perfactly,support Chinese Language',
    url='TODO',
    author='TODO',
    author_email='TODO',
    license='MIT',
    include_package_data=True,
    install_requires=[
        # "click",
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
    keywords='TODO',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'head = pylinux.editor:head',
            'tail = pylinux.editor:tail',
        ]
    },
)