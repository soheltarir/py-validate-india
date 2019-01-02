from setuptools import setup

setup(
    name='validate-india',
    version='1.0.0',
    packages=['validate_india'],
    url='https://github.com/soheltarir/py-validate-india',
    license='Apache-2.0',
    author='Sohel Tarir',
    author_email='sohel.tarir@gmail.com',
    description='Python module to validate and extract Indian Mobile, Aadhaar, GST, PAN, etc.',
    keywords=['India', 'Indian', 'Mobile', 'Aadhaar', 'PAN', 'GST'],
    classifiers={
        '5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)
