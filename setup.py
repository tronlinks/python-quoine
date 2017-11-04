from distutils.core import setup

version = '0.0.1'

setup(
    name='quoine',
    version=version,
    description='(Unofficial) Python bindings for Quoinex/Qryptos API',
    author='Sean Lim',
    author_email='seanlim0101@gmail.com',
    url='https://github.com/seanlim1/python-quoine',
    license='MIT',
    packages=['quoine'],
    install_requires=[
        'requests',
        'pyjwt'
    ],
    keywords=['quoine', 'quoinex', 'qryptos', 'api'
              'bitcoin', 'ethereum', 'cryptocurrency'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial'
    ]
)
