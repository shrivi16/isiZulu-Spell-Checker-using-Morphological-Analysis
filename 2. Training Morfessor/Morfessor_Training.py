import morfessor

# Note it takes approximately 1.5 hours for training to be done

io = morfessor.MorfessorIO()

# Loading in our prepared dataset that was created under the 'Dataset Preparation' directory
train_data = list(io.read_corpus_file('Dataset.txt'))

model_tokens = morfessor.BaselineModel()

model_tokens.load_data(train_data)

model_tokens.train_batch()

# writing our model as a bin file as morfessor saves its model in this format
io.write_binary_model_file("MorfessorModel.bin", model_tokens)
