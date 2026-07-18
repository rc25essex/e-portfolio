from unittest.mock import Mock

from ai_application import (
    AIApplication,
    AIServiceFactory,
    OpenAIFactory,
    AzureAIFactory,
    OpenAITextModel,
    OpenAIEmbeddingModel,
    AzureTextModel,
    AzureEmbeddingModel,
)


# Factory creation tests

def test_openai_factory_creates_openai_family():
    factory = OpenAIFactory()

    assert isinstance(factory.create_text_model(), OpenAITextModel)
    assert isinstance(
        factory.create_embedding_model(),
        OpenAIEmbeddingModel,
    )


def test_azure_factory_creates_azure_family():
    factory = AzureAIFactory()

    assert isinstance(factory.create_text_model(), AzureTextModel)
    assert isinstance(
        factory.create_embedding_model(),
        AzureEmbeddingModel,
    )


# Mocking test

def test_ai_application_uses_mocked_models(capsys):
    mock_text_model = Mock()
    mock_embedding_model = Mock()

    mock_text_model.generate_text.return_value = "Mock text response"
    mock_embedding_model.create_embedding.return_value = "Mock embedding"

    mock_factory = Mock(spec=AIServiceFactory)
    mock_factory.create_text_model.return_value = mock_text_model
    mock_factory.create_embedding_model.return_value = (
        mock_embedding_model
    )

    application = AIApplication(mock_factory)
    application.run()

    mock_factory.create_text_model.assert_called_once()
    mock_factory.create_embedding_model.assert_called_once()

    mock_text_model.generate_text.assert_called_once_with(
        "Explain design patterns"
    )
    mock_embedding_model.create_embedding.assert_called_once_with(
        "Advanced OO design"
    )

    output = capsys.readouterr().out

    assert "Mock text response" in output
    assert "Mock embedding" in output
