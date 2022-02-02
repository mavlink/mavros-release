%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-mavros-extras
Version:        2.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mavros_extras package

License:        GPLv3
URL:            http://wiki.ros.org/mavros_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       GeographicLib
Requires:       GeographicLib-devel
Requires:       eigen3-devel
Requires:       ros-rolling-diagnostic-msgs
Requires:       ros-rolling-diagnostic-updater
Requires:       ros-rolling-eigen-stl-containers
Requires:       ros-rolling-eigen3-cmake-module
Requires:       ros-rolling-geographic-msgs
Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-libmavconn
Requires:       ros-rolling-mavlink
Requires:       ros-rolling-mavros
Requires:       ros-rolling-mavros-msgs
Requires:       ros-rolling-message-filters
Requires:       ros-rolling-nav-msgs
Requires:       ros-rolling-pluginlib
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-rosidl-default-runtime
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-std-srvs
Requires:       ros-rolling-tf2-eigen
Requires:       ros-rolling-tf2-ros
Requires:       ros-rolling-trajectory-msgs
Requires:       ros-rolling-urdf
Requires:       ros-rolling-visualization-msgs
Requires:       ros-rolling-yaml-cpp-vendor
Requires:       yaml-cpp-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  GeographicLib
BuildRequires:  GeographicLib-devel
BuildRequires:  eigen3-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-gmock
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-cmake-python
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-angles
BuildRequires:  ros-rolling-diagnostic-msgs
BuildRequires:  ros-rolling-diagnostic-updater
BuildRequires:  ros-rolling-eigen-stl-containers
BuildRequires:  ros-rolling-eigen3-cmake-module
BuildRequires:  ros-rolling-geographic-msgs
BuildRequires:  ros-rolling-geometry-msgs
BuildRequires:  ros-rolling-libmavconn
BuildRequires:  ros-rolling-mavlink
BuildRequires:  ros-rolling-mavros
BuildRequires:  ros-rolling-mavros-msgs
BuildRequires:  ros-rolling-message-filters
BuildRequires:  ros-rolling-nav-msgs
BuildRequires:  ros-rolling-pluginlib
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  ros-rolling-std-srvs
BuildRequires:  ros-rolling-tf2-eigen
BuildRequires:  ros-rolling-tf2-ros
BuildRequires:  ros-rolling-trajectory-msgs
BuildRequires:  ros-rolling-urdf
BuildRequires:  ros-rolling-visualization-msgs
BuildRequires:  ros-rolling-yaml-cpp-vendor
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Extra nodes and plugins for MAVROS.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Feb 02 2022 Vladimir Ermakov <vooon341@gmail.com> - 2.1.0-1
- Autogenerated by Bloom

* Sun Nov 28 2021 Vladimir Ermakov <vooon341@gmail.com> - 2.0.5-1
- Autogenerated by Bloom

* Thu Nov 04 2021 Vladimir Ermakov <vooon341@gmail.com> - 2.0.4-1
- Autogenerated by Bloom

