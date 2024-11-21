from transformers import GPT2Tokenizer, GPT2Model
import torch
import os

cache_dir = "./gpt2_model_cache"

def get_all_gpt_tokens():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    vocab = tokenizer.get_vocab()
    tokens = list(vocab.keys())
    # Display the first 20 tokens
    print(tokens[:20])

    # Save all tokens to a file
    with open("gpt2_tokens.txt", "w") as f:
        for token in tokens:
            f.write(token + "\n")

def get_tokens_from_text(text):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    # Get token IDs (numerical form)
    token_ids = tokenizer.encode(text)

    # Get the actual tokens (text form)
    tokens = tokenizer.tokenize(text)

    print("Tokens:", tokens)
    # print("Token IDs:", token_ids)
    return (tokens, token_ids)

def get_embedding_vectors(text):
    # Load GPT-2 tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2", cache_dir=cache_dir)
    model = GPT2Model.from_pretrained("gpt2", cache_dir=cache_dir)
    inputs = tokenizer(text, return_tensors="pt")  # Convert text to files tensor
    # Pass inputs to the model to get embeddings
    with torch.no_grad():
        outputs = model(**inputs)

    # The embedding vectors are in the `last_hidden_state` tensor
    embeddings = outputs.last_hidden_state
    # print("Shape of embeddings:", embeddings.shape)
    # print("Embedding vectors:", embeddings)
    return embeddings.mean(dim=1)

def save_embedding_vecotr():
    # Step 2: Download and save the GPT-2 tokenizer and model to the cache directory
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2", cache_dir=cache_dir)
    model = GPT2Model.from_pretrained("gpt2", cache_dir=cache_dir)

def compute_dot_product_of_difference(text1, text2, text3, text4):
    get_tokens_from_text(text1)
    A = get_embedding_vectors(text1)
    # A = A / A.norm()

    get_tokens_from_text(text2)
    B = get_embedding_vectors(text2)
    # B = B / B.norm()

    get_tokens_from_text(text3)
    C = get_embedding_vectors(text3)
    # C = C / C.norm()

    get_tokens_from_text(text4)
    D = get_embedding_vectors(text4)
    # D = D / D.norm()

    # Step 1: Compute the differences
    diff1 = A - B  # Shape (1, 1, 768)
    diff2 = C - D  # Shape (1, 1, 768)

    # Step 2: Flatten the tensors to 1D vectors for dot product calculation
    diff1_flat = diff1.view(-1)  # Shape (768,)
    diff2_flat = diff2.view(-1)  # Shape (768,)

    # Step 3: Compute the dot product
    dot_product = torch.dot(diff1_flat, diff2_flat)

    # Step 4: Print the result
    print("Dot product:", dot_product.item())
    return dot_product


# save_embedding_vecotr()

compute_dot_product_of_difference("boy", "girl", "man", "woman")
compute_dot_product_of_difference("king", "queen", "man", "woman")
compute_dot_product_of_difference("uncle", "aunt", "man", "woman")
compute_dot_product_of_difference("tiger", "tigress", "man", "woman")
compute_dot_product_of_difference("Russia", "Ukraine", "man", "woman")



