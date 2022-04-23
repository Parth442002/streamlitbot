from trainingdata import training_dataset
from chatterbot import ChatBot
import chatterbot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

Bot1 = ChatBot(
    name='Bot1',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///bot1.sqlite3',
    statement_comparison_function=LevenshteinDistance(),
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
    ],
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.SpecificResponseAdapter",
    ],
)

corpus_trainer = ChatterBotCorpusTrainer(Bot1)
corpus_trainer.train('chatterbot.corpus.english')
corpus_trainer.train('chatterbot.corpus.hindi')
corpus_trainer.train('chatterbot.corpus.telugu')


list_trainer = ListTrainer(Bot1)
list_trainer.train(training_dataset)
