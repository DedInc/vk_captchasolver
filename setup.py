import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='vk_captchasolver',
    version='1.0.0',
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
    packages=['vk_captchasolver'],
    include_package_data = True,
    install_requires = ['Pillow', 'onnxruntime', 'numpy', 'requests'],
    data_files = [('vk_captchasolver',  ['vk_captchasolver/captcha_model.onnx', 'vk_captchasolver/ctc_model.onnx'])],
    python_requires='>=3.6'
)