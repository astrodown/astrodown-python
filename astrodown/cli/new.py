import enum


class ComponentType(str, enum.Enum):
    analysis = "analysis"
    dataset = "dataset"
    model = "model"
    shinyapp = "shinyapp"
    api = "api"
