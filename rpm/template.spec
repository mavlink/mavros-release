Name:           ros-jade-mavros-extras
Version:        0.11.1
Release:        0%{?dist}
Summary:        ROS mavros_extras package

Group:          Development/Libraries
License:        GPLv3
URL:            http://wiki.ros.org/mavros_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       python
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-image-transport
Requires:       ros-jade-mavlink
Requires:       ros-jade-mavros
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-mavlink
BuildRequires:  ros-jade-mavros
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-visualization-msgs

%description
Extra nodes and plugins for mavros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Apr 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue Mar 24 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.11.0-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 0.10.2-0
- Autogenerated by Bloom

