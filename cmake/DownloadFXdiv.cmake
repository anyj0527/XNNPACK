# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# Copyright 2019 Google LLC
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

CMAKE_MINIMUM_REQUIRED(VERSION 3.5 FATAL_ERROR)

PROJECT(fxdiv-download NONE)

INCLUDE(ExternalProject)
ExternalProject_Add(fxdiv
  URL "${CMAKE_SOURCE_DIR}/externals/fxdiv.tar.gz"
  SOURCE_DIR "${CMAKE_BINARY_DIR}/FXdiv-source"
  BINARY_DIR "${CMAKE_BINARY_DIR}/FXdiv"
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
  TEST_COMMAND ""
)

INCLUDE(ExternalProject)
ExternalProject_Add(psimd
  URL "${CMAKE_SOURCE_DIR}/externals/psimd.tar.gz"
  SOURCE_DIR "${CMAKE_BINARY_DIR}/psimd-source"
  BINARY_DIR "${CMAKE_BINARY_DIR}/psimd"
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
  INSTALL_COMMAND ""
  TEST_COMMAND ""
)
