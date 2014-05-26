reem_iri_poseslam
=================

Necessary stuff to install and run poseslam with the REEM robot


# Instructions to install:

Setup system
```
source /opt/ros/hydro/setup.bash
```

Setup REEM environment
You must have followed the tutorial on how to install REEM simulation:

http://wiki.ros.org/Robots/REEM/Tutorials/Launching%20a%20REEM%20Gazebo%20simulation
```
source ~/reem-sim_ws/devel/setup.bash
```

Create a workspace
```
mkdir -p ~/poseslam_ws/src && cd ~/poseslam_ws/src
catkin_init_workspace
```

Download eigen 3.2 (if it's not your system version, on ubuntu 12.04 it's 3.0.5 by default)
```
wget http://bitbucket.org/eigen/eigen/get/3.2.1.tar.gz
```
Extract (it will generate eigen-eigen-6b38706d90a9 folder)
```
tar -xvf 3.2.1.tar.gz
```

Checkout poseSLAM stuff
```
cd ~/poseslam_ws/src
wstool init .
wstool merge https://raw.githubusercontent.com/awesomebytes/reem_iri_poseslam/master/poseslam.rosinstall
wstool up -j4
```

Change in poseSLAM/FindposeSLAM.cmake poseslam_local_path to your path.
SET(poseslam_local_path ~/poseslam_ws/src/poseSLAM)
TODO: This should be fixed someway

Setup Eigen in this shell
```
export CMAKE_PREFIX_PATH=~/poseslam_ws/src/eigen-eigen-6b38706d90a9:$CMAKE_PREFIX_PATH
export CMAKE_MODULE_PATH=~/poseslam_ws/src/eigen-eigen-6b38706d90a9/cmake:~/poseslam_ws/src/poseSLAM:$CMAKE_MODULE_PATH
```

Compile poseSLAM
```
cd ~/poseslam_ws/src/poseSLAM/build
cmake ..
make
```

Test if we have all the dependences
```
rosdep install --from-paths src --ignore-src --rosdistro hydro -y
```


Compile ROS stuff 
```
source ~/reem-sim_ws/devel/setup.bash
cd ~/poseslam_ws
catkin_make --only-pkg-with-deps iri_poseslam --cmake-args -DCMAKE_MODULE_PATH=~/poseslam_ws/src/poseSLAM
catkin_make
```

=================

# How to launch REEM and poseSLAM:

Remember to source our workspace first in any terminal you will use:

```
source ~/poseslam_ws/devel/setup.bash
```

Now launch a REEM simulation:
```
roslaunch reem_iri_poseslam reem_simulation.launch
```

Launch poseSLAM and it's needed stuff (odom to odom_rel):
```
roslaunch reem_iri_poseslam poseslam_occ_REEM.launch
```


Launch a Rviz to see what is happening:
```
rosrun rviz  rviz -d `rospack find reem_iri_poseslam`/config/reem_and_poseslam.rviz
```

Finally you can teleop the robot from another terminal running:
```
rosrun reem_iri_poseslam key_teleop.py
```

(Note that the window must be in focus when pressing the arrows of the keyboard).