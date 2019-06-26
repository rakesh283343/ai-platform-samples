#!/usr/bin/env python
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'tensorflow==1.13.1',
    'tensorflow-model-analysis==0.13.2'
]

setup(
    name='trainer',
    description='AI Platform Training job for TensorFlow',
    author='Google Cloud Platform',
    install_requires=REQUIRED_PACKAGES,
    version='0.1',
    packages=find_packages(),
    include_package_data=True
)