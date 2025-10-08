from transformers import BertTokenizer, TFBertForSequenceClassification

def build_bert_model():
    model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    return model, tokenizer
