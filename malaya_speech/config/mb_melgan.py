config = {
    'sampling_rate': 22050,
    'hop_size': 256,
    'melgan_generator_params': {
        'out_channels': 4,
        'kernel_size': 7,
        'filters': 384,
        'upsample_scales': [8, 4, 2],
        'stack_kernel_size': 3,
        'stacks': 4,
        'is_weight_norm': False,
    },
    'melgan_discriminator_params': {
        'out_channels': 1,
        'scales': 3,
        'downsample_pooling': 'AveragePooling1D',
        'downsample_pooling_params': {'pool_size': 4, 'strides': 2},
        'kernel_sizes': [5, 3],
        'filters': 16,
        'max_downsample_filters': 512,
        'downsample_scales': [4, 4, 4],
        'nonlinear_activation': 'LeakyReLU',
        'nonlinear_activation_params': {'alpha': 0.2},
        'is_weight_norm': False,
    },
    'lambda_feat_match': 10.0,
    'batch_size': 16,
    'batch_max_steps': 8192,
    'batch_max_steps_valid': 81920,
    'remove_short_samples': True,
    'allow_cache': True,
    'is_shuffle': True,
    'generator_optimizer_params': {'lr': 0.0001, 'beta_1': 0.5, 'beta_2': 0.9},
    'discriminator_optimizer_params': {
        'lr': 0.0001,
        'beta_1': 0.5,
        'beta_2': 0.9,
    },
    'train_max_steps': 4000000,
    'save_interval_steps': 3,
    'eval_interval_steps': 2,
    'log_interval_steps': 1,
    'discriminator_train_start_steps': 0,
    'num_save_intermediate_results': 1,
    'stft_loss_params': {
        'fft_lengths': [1024, 2048, 512],
        'frame_steps': [120, 240, 50],
        'frame_lengths': [600, 1200, 240],
    },
    'subband_stft_loss_params': {
        'fft_lengths': [384, 683, 171],
        'frame_steps': [30, 60, 10],
        'frame_lengths': [150, 300, 60],
    },
}
