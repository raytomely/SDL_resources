from distutils.core import setup, Extension
from setuptools.command.build_ext import build_ext
import os, sysconfig

path="C:\\Users\\MB\\AppData\\Local\\Programs\\Python\\Python38-32\\"

# Common flags for both release and debug builds.
extra_compile_args = ["-std=c++11", "-Wall", "-Wextra"]

def main():
    setup(name="fputs",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="<your name>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("fputs", ["fputsmodule.c"],
                                 library_dirs = [os.getcwd(),path],
                                 extra_compile_args=extra_compile_args,
                                 extra_link_args=["-undefined"],)],)

if __name__ == "__main__":
    main()
