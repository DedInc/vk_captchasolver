from setuptools import setup, find_packages
from os import name as osn

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vk_captchasolver',
    version='1.0.4',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='VKontakte captcha solver with 91% accuracy right.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/vk_captchasolver',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/vk_captchasolver/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
	install_requires = ['Pillow', 'numpy', 'requests', 'onnxruntime==1.9.0' if osn == 'nt' else 'onnxruntime>=1.9.0'],
    python_requires='>=3.6'
)