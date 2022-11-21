# COPYRIGHT 1995-2021 ESRI
# TRADE SECRETS: ESRI PROPRIETARY AND CONFIDENTIAL
# Unpublished material - all rights reserved under the
# Copyright Laws of the United States and applicable international
# laws, treaties, and conventions.
#
# For additional information, contact:
# Environmental Systems Research Institute, Inc.
# Attn: Contracts and Legal Services Department
# 380 New York Street
# Redlands, California, 92373
# USA
#
# email: contracts@esri.com

cmake_minimum_required(VERSION 3.20)

project(ActionsTest CXX C)

# -----------------------------------------------------------------------------
# Global settings and options for the entire project
# -----------------------------------------------------------------------------

# set(CMAKE_VERBOSE_MAKEFILE ON)
include(cmake/CPM.cmake)

CPMAddPackage(
  NAME catch2
  GITHUB_REPOSITORY catchorg/Catch2
  VERSION 3.1.0
)

add_executable(tests test.cpp)

target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)
