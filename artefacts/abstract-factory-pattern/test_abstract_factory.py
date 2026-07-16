from ai_application import (
    OpenAIFactory,
    AzureAIFactory,
    OpenAITextModel,
    OpenAIEmbeddingModel,
    AzureTextModel,
    AzureEmbeddingModel,
)

def test_openai_factory_creates_openai_family():
    factory = OpenAIFactory()

    assert isinstance(factory.create_text_model(), OpenAITextModel)
    assert isinstance(
        factory.create_embedding_model(),
        OpenAIEmbeddingModel
    )


def test_azure_factory_creates_azure_family():
    factory = AzureAIFactory()

    assert isinstance(factory.create_text_model(), AzureTextModel)
    assert isinstance(
        factory.create_embedding_model(),
        AzureEmbeddingModel
    )
