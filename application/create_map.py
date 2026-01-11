from pathlib import Path
import hydra
from omegaconf import DictConfig
from vlmaps.map.vlmap import VLMap
import os


@hydra.main(
    version_base=None,
    config_path="../config",
    config_name="map_creation_cfg.yaml",
)
def main(config: DictConfig) -> None:
    vlmap = VLMap(config.map_config)
    data_dir = Path(config.data_paths.vlmaps_data_dir)
    data_dirs = sorted([x for x in data_dir.iterdir() if x.is_dir()])

    # vlmap.create_map(data_dirs[config.scene_id])
        # vlmap.create_map(data_dirs[config.scene_id])
    scene_dir = os.path.join(data_dir, config.scene_name)
    print(scene_dir)
    vlmap.create_map(scene_dir)



if __name__ == "__main__":
    main()
