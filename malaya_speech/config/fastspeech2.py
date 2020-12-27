config = {
    'n_speakers': 1,
    'encoder_hidden_size': 384,
    'encoder_num_hidden_layers': 4,
    'encoder_num_attention_heads': 2,
    'encoder_attention_head_size': 192,
    'encoder_intermediate_size': 1024,
    'encoder_intermediate_kernel_size': 3,
    'encoder_hidden_act': 'mish',
    'decoder_hidden_size': 384,
    'decoder_num_hidden_layers': 4,
    'decoder_num_attention_heads': 2,
    'decoder_attention_head_size': 192,
    'decoder_intermediate_size': 1024,
    'decoder_intermediate_kernel_size': 3,
    'decoder_hidden_act': 'mish',
    'variant_prediction_num_conv_layers': 2,
    'variant_predictor_filter': 256,
    'variant_predictor_kernel_size': 3,
    'variant_predictor_dropout_rate': 0.5,
    'num_mels': 80,
    'hidden_dropout_prob': 0.2,
    'attention_probs_dropout_prob': 0.1,
    'max_position_embeddings': 2048,
    'initializer_range': 0.02,
    'output_attentions': False,
    'output_hidden_states': False,
}
