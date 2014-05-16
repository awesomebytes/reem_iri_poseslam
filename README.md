reem_iri_poseslam
=================

Necessary stuff to install and run poseslam with the REEM robot


Instructions to install:

# Setup system
source /opt/ros/hydro/setup.bash

# Setup REEM environment
You must have followed the tutorial on how to install REEM simulation:
http://wiki.ros.org/Robots/REEM/Tutorials/Launching%20a%20REEM%20Gazebo%20simulation
```
source ~/reem-sim_ws/devel/setup.bash
```

# Create a workspace
```
mkdir -p ~/poseslam_ws/src && cd ~/poseslam_ws/src
catkin_init_workspace
```

# Download eigen 3.2 (if it's not your system version, on ubuntu 12.04 it's 3.0.5 by default)
```
wget http://bitbucket.org/eigen/eigen/get/3.2.1.tar.gz
```
# Extract (it will generate eigen-eigen-6b38706d90a9 folder)
```
tar -xvf 3.2.1.tar.gz
```

# Checkout poseSLAM stuff
```
cd ~/poseslam_ws/src
wstool init .
wstool merge https://raw.githubusercontent.com/awesomebytes/reem_iri_poseslam/master/poseslam.rosinstall
wstool up -j4
```

# Change in poseSLAM/FindposeSLAM.cmake "~/iri-lab/labrobotica/algorithms/poseSLAM" for "~/poseslam_ws/src/poseSLAM/lib"
# TODO: This should be fixed someway

# Setup Eigen in this shell
```
export CMAKE_PREFIX_PATH=~/poseslam_ws/src/eigen-eigen-6b38706d90a9:$CMAKE_PREFIX_PATH
export CMAKE_MODULE_PATH=~/poseslam_ws/src/eigen-eigen-6b38706d90a9/cmake:$CMAKE_MODULE_PATH
```

# Compile poseSLAM
```
cd ~/poseslam_ws/src/poseSLAM/build
cmake ..
make
```
# Compile ROS stuff
cd ~/poseslam_ws
catkin_make


