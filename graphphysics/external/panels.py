import torch
from torch_geometric.data import Data
from graphphysics.utils.nodetype import NodeType

device = "cuda" if torch.cuda.is_available() else "cpu"


def build_mask_wallbc(node_type: torch.Tensor):
    mask = torch.logical_or(
        node_type == NodeType.WALL_BOUNDARY, node_type == NodeType.OBSTACLE
    )
    return mask


def build_features(graph: Data) -> Data:
    # construct features
    current_velocity = graph.x[:, 0:2]
    pressure = graph.x[:, 3].unsqueeze(1)
    levelset = graph.x[:, 4].unsqueeze(1)
    nodetype = graph.x[:, 5].unsqueeze(1)

    # wall bc: set velocity to 0
    wallbc_mask = build_mask_wallbc(nodetype.squeeze())
    current_velocity[wallbc_mask] = 0.0

    graph.x = torch.cat(
        (
            current_velocity,
            pressure,
            levelset,
            graph.pos[:, 0:2],
            nodetype,
        ),
        dim=1,
    )

    # hide Vz in target
    target_velocity = graph.y[:, 0:2]
    target_pressure = graph.y[:, 3].unsqueeze(1)
    graph.y = torch.cat((target_velocity, target_pressure), dim=1)

    return graph
