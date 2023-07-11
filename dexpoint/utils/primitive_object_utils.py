import sapien.core as sapien
from sapien.utils import Viewer
import numpy as np


def create_box(
        scene: sapien.Scene,
        half_size,
        color=None,
        name='',
        visual_only=False,
) -> sapien.Actor:
    """Create a box.

    Args:
        scene: sapien.Scene to create a box.
        pose: 6D pose of the box.
        half_size: [3], half size along x, y, z axes.
        color: [3] or [4], rgb or rgba
        name: name of the actor.

    Returns:
        sapien.Actor
    """
    half_size = np.array(half_size)
    builder: sapien.ActorBuilder = scene.create_actor_builder()
    if not visual_only:
        builder.add_box_collision(half_size=half_size)  # Add collision shape
    builder.add_box_visual(half_size=half_size, color=color)  # Add visual shape
    box: sapien.Actor = builder.build(name=name)
    return box

def create_capsule(
        scene: sapien.Scene,
        radius,
        half_length,
        color=None,
        visual_only=False,
        name='',
) -> sapien.Actor:
    """Create a capsule (x-axis <-> half_length). See create_box."""
    builder = scene.create_actor_builder()
    if not visual_only:
        builder.add_capsule_collision(radius=radius, half_length=half_length)
    builder.add_capsule_visual(radius=radius, half_length=half_length, color=color)
    capsule = builder.build(name=name)
    return capsule

def create_sphere(
        scene: sapien.Scene,
        pose: sapien.Pose,
        radius,
        color=None,
        name='',
) -> sapien.Actor:
    """Create a sphere. See create_box."""
    builder = scene.create_actor_builder()
    builder.add_sphere_collision(radius=radius)
    builder.add_sphere_visual(radius=radius, color=color)
    sphere = builder.build(name=name)
    sphere.set_pose(pose)
    return sphere