cmake_minimum_required(VERSION 3.5)
project(uuv_gazebo_worlds)

find_package(ament_cmake REQUIRED)

install(DIRECTORY models
        DESTINATION share/${PROJECT_NAME}
        PATTERN "*~" EXCLUDE)

ament_environment_hooks("hooks/resource_paths.dsv.in")

ament_package()
