%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-mavros
Version:        2.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mavros package

License:        GPLv3
URL:            http://wiki.ros.org/mavros
Source0:        %{name}-%{version}.tar.gz

Requires:       GeographicLib
Requires:       GeographicLib-devel
Requires:       console-bridge-devel
Requires:       eigen3-devel
Requires:       python%{python3_pkgversion}-click
Requires:       ros-galactic-diagnostic-msgs
Requires:       ros-galactic-diagnostic-updater
Requires:       ros-galactic-eigen-stl-containers
Requires:       ros-galactic-eigen3-cmake-module
Requires:       ros-galactic-geographic-msgs
Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-libmavconn
Requires:       ros-galactic-mavlink
Requires:       ros-galactic-mavros-msgs
Requires:       ros-galactic-message-filters
Requires:       ros-galactic-nav-msgs
Requires:       ros-galactic-pluginlib
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-components
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-rcpputils
Requires:       ros-galactic-rosidl-default-runtime
Requires:       ros-galactic-sensor-msgs
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-std-srvs
Requires:       ros-galactic-tf2-eigen
Requires:       ros-galactic-tf2-ros
Requires:       ros-galactic-trajectory-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  GeographicLib
BuildRequires:  GeographicLib-devel
BuildRequires:  console-bridge-devel
BuildRequires:  eigen3-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-cmake-gmock
BuildRequires:  ros-galactic-ament-cmake-gtest
BuildRequires:  ros-galactic-ament-cmake-pytest
BuildRequires:  ros-galactic-ament-cmake-python
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-angles
BuildRequires:  ros-galactic-diagnostic-msgs
BuildRequires:  ros-galactic-diagnostic-updater
BuildRequires:  ros-galactic-eigen-stl-containers
BuildRequires:  ros-galactic-eigen3-cmake-module
BuildRequires:  ros-galactic-geographic-msgs
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-libmavconn
BuildRequires:  ros-galactic-mavlink
BuildRequires:  ros-galactic-mavros-msgs
BuildRequires:  ros-galactic-message-filters
BuildRequires:  ros-galactic-nav-msgs
BuildRequires:  ros-galactic-pluginlib
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-components
BuildRequires:  ros-galactic-rcpputils
BuildRequires:  ros-galactic-sensor-msgs
BuildRequires:  ros-galactic-std-msgs
BuildRequires:  ros-galactic-std-srvs
BuildRequires:  ros-galactic-tf2-eigen
BuildRequires:  ros-galactic-tf2-ros
BuildRequires:  ros-galactic-trajectory-msgs
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for Ground
Control Station.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Wed Feb 02 2022 Vladimir Ermakov <vooon341@gmail.com> - 2.1.0-1
- Autogenerated by Bloom

* Sun Nov 28 2021 Vladimir Ermakov <vooon341@gmail.com> - 2.0.5-1
- Autogenerated by Bloom

* Thu Nov 04 2021 Vladimir Ermakov <vooon341@gmail.com> - 2.0.4-1
- Autogenerated by Bloom

* Sun Jun 20 2021 Vladimir Ermakov <vooon341@gmail.com> - 2.0.3-1
- Autogenerated by Bloom

