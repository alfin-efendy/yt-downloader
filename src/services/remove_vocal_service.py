from audio_separator.separator import Separator

class RemoveVocalService:
    @staticmethod
    async def remove_vocals(file_path: str):
        # Initialize the Separator class (with optional configuration properties, below)
        separator = Separator()

        # Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
        separator.load_model()

        # Perform the separation on specific audio files without reloading the model
        output_files = separator.separate(file_path)

        return output_files