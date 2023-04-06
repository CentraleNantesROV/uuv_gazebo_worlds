from simple_launch import SimpleLauncher
import os

sl = SimpleLauncher(use_sim_time = False)

sl.declare_arg('model', 'none')


def launch_setup():

    models = [m for m in os.listdir(os.path.dirname(__file__)) if not m.endswith('.py')]
    name = sl.arg('model')

    if name not in models:
        print('Give a model name, available models are:', models)
    else:

        with sl.group(ns = name):
            sl.robot_state_publisher('uuv_gazebo_worlds',
                                    description_dir = 'models/' + name,
                                    description_file = 'model.sdf')

    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
