from abc import ABC, abstractmethod


# Product interfaces
class TextModel(ABC):
    @abstractmethod
    def generate_text(self, prompt):
        pass


class EmbeddingModel(ABC):
    @abstractmethod
    def create_embedding(self, text):
        pass


# OpenAI product family
class OpenAITextModel(TextModel):
    def generate_text(self, prompt):
        return f"OpenAI text response for: {prompt}"


class OpenAIEmbeddingModel(EmbeddingModel):
    def create_embedding(self, text):
        return f"OpenAI embedding for: {text}"


# Azure AI product family
class AzureTextModel(TextModel):
    def generate_text(self, prompt):
        return f"Azure AI text response for: {prompt}"


class AzureEmbeddingModel(EmbeddingModel):
    def create_embedding(self, text):
        return f"Azure AI embedding for: {text}"


# Abstract Factory
class AIServiceFactory(ABC):
    @abstractmethod
    def create_text_model(self):
        pass

    @abstractmethod
    def create_embedding_model(self):
        pass


# Concrete factories
class OpenAIFactory(AIServiceFactory):
    def create_text_model(self):
        return OpenAITextModel()

    def create_embedding_model(self):
        return OpenAIEmbeddingModel()


class AzureAIFactory(AIServiceFactory):
    def create_text_model(self):
        return AzureTextModel()

    def create_embedding_model(self):
        return AzureEmbeddingModel()


# Client code
class AIApplication:
    def __init__(self, factory):
        self.text_model = factory.create_text_model()
        self.embedding_model = factory.create_embedding_model()

    def run(self):
        print(self.text_model.generate_text("Explain design patterns"))
        print(self.embedding_model.create_embedding("Advanced OO design"))


provider = "azure"

if provider == "openai":
    factory = OpenAIFactory()
elif provider == "azure":
    factory = AzureAIFactory()
else:
    raise ValueError("Unsupported AI provider")

application = AIApplication(factory)
application.run()
