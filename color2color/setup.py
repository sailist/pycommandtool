from setuptools import setup,find_packages

setup(
    name='Sailist',
    version='0.6.8.dev1',
    description='convert markdown 2 latex code perfactly,support Chinese Language',
    url='TODO',
    author='sailist',
    author_email='sailist@outlook.com',
    license='MIT',
    include_package_data = True,
    install_requires = [
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
    keywords='color convert',
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'cdc = color2color.cdc:main'
        ]
      },
)