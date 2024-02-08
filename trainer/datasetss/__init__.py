from hydra.core.config_store import ConfigStore

from trainer.datasetss.clip_hf_dataset import CLIPHFDatasetConfig, PickapicOnlySomeDatasetConfig

cs = ConfigStore.instance()
cs.store(group="dataset", name="clip", node=CLIPHFDatasetConfig)
cs.store(group="dataset", name="pickapick_only_some", node=PickapicOnlySomeDatasetConfig)
