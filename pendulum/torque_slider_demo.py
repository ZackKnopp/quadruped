import argparse
import numpy as np

from pydrake.all import DiagramBuilder, Simulator
from pydrake.examples.pendulum import PendulumPlant
from underactuated import SliderSystem
from visualizer import PendulumVisualizer

builder = DiagramBuilder()
pendulum = builder.AddSystem(PendulumPlant())

parser = argparse.ArgumentParser()
parser.add_argument(
    "-T", "--duration", type=float, help="Duration to run sim.", default=10000.0
)
args = parser.parse_args()

visualizer = builder.AddSystem(PendulumVisualizer())
builder.Connect(pendulum.get_output_port(0), visualizer.get_input_port(0))

ax = visualizer.fig.add_axes([0.2, 0.95, 0.6, 0.025])
torque_system = builder.AddSystem(SliderSystem(ax, "Torque", -5.0, 5.0))
builder.Connect(torque_system.get_output_port(0), pendulum.get_input_port(0))

diagram = builder.Build()
simulator = Simulator(diagram)
simulator.set_target_realtime_rate(1.0)
simulator.set_publish_every_time_step(False)

context = simulator.get_mutable_context()
context.SetContinuousState([1.0, 0.0])

simulator.StepTo(args.duration)
