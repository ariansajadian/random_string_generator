from distutils.core import setup
setup(
  name = 'randoms_string_generator',         # How you named your package folder (MyLib)
  packages = ['randoms_string_generator'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Generate verification code and random password',   # Give a short description about your library
  author = 'Arian',                   # Type in your name
  author_email = 'ariansajadian79@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ariansajadian/randoms_string_generator.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ariansajadian/randoms_string_generator/archive/refs/tags/v1.0.0.tar.gz',    # I explain this later on
  keywords = ['String', 'Random', 'Code'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)