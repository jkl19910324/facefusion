from collections import namedtuple
from typing import Any, Callable, Dict, List, Literal, Optional, Tuple, TypedDict

import numpy
from numpy.typing import NDArray

Score = float
Angle = int

BoundingBox = NDArray[Any]
FaceLandmark5 = NDArray[Any]
FaceLandmark68 = NDArray[Any]
FaceLandmarkSet = TypedDict('FaceLandmarkSet',
{
	'5' : FaceLandmark5, #type:ignore[valid-type]
	'5/68' : FaceLandmark5, #type:ignore[valid-type]
	'68' : FaceLandmark68, #type:ignore[valid-type]
	'68/5' : FaceLandmark68 #type:ignore[valid-type]
})
FaceScoreSet = TypedDict('FaceScoreSet',
{
	'detector' : Score,
	'landmarker' : Score
})
Embedding = NDArray[numpy.float64]
Face = namedtuple('Face',
[
	'bounding_box',
	'landmark_set',
	'score_set',
	'angle',
	'embedding',
	'normed_embedding',
	'gender',
	'age'
])
FaceSet = Dict[str, List[Face]]
FaceStore = TypedDict('FaceStore',
{
	'static_faces' : FaceSet,
	'reference_faces': FaceSet
})

VisionFrame = NDArray[Any]
Mask = NDArray[Any]
Points = NDArray[Any]
Distance = NDArray[Any]
Matrix = NDArray[Any]
Translation = NDArray[Any]

AudioBuffer = bytes
Audio = NDArray[Any]
AudioChunk = NDArray[Any]
AudioFrame = NDArray[Any]
Spectrogram = NDArray[Any]
MelFilterBank = NDArray[Any]

Fps = float
Padding = Tuple[int, int, int, int]
Resolution = Tuple[int, int]

ProcessState = Literal['checking', 'processing', 'stopping', 'pending']
QueuePayload = TypedDict('QueuePayload',
{
	'frame_number' : int,
	'frame_path' : str
})
UpdateProgress = Callable[[int], None]
ProcessFrames = Callable[[List[str], List[QueuePayload], UpdateProgress], None]
ProcessStep = Callable[[Dict[str, Any]], bool]
Args = Dict[str, Any]

Content = Dict[Any, Any]

WarpTemplate = Literal['arcface_112_v1', 'arcface_112_v2', 'arcface_128_v2', 'ffhq_512']
WarpTemplateSet = Dict[WarpTemplate, NDArray[Any]]
ProcessMode = Literal['output', 'preview', 'stream']

ErrorCode = Literal[0, 1, 2, 3, 4]
LogLevel = Literal['error', 'warn', 'info', 'debug']

TableHeaders = List[str]
TableContents = List[List[int | float | str]]

VideoMemoryStrategy = Literal['strict', 'moderate', 'tolerant']
FaceDetectorModel = Literal['many', 'retinaface', 'scrfd', 'yoloface']
FaceDetectorSet = Dict[FaceDetectorModel, List[str]]
FaceRecognizerModel = Literal['arcface_blendswap', 'arcface_ghost', 'arcface_inswapper', 'arcface_simswap', 'arcface_uniface']
FaceSelectorMode = Literal['many', 'one', 'reference']
FaceSelectorOrder = Literal['left-right', 'right-left', 'top-bottom', 'bottom-top', 'small-large', 'large-small', 'best-worst', 'worst-best']
FaceSelectorAge = Literal['child', 'teen', 'adult', 'senior']
FaceSelectorGender = Literal['female', 'male']
FaceMaskType = Literal['box', 'occlusion', 'region']
FaceMaskRegion = Literal['skin', 'left-eyebrow', 'right-eyebrow', 'left-eye', 'right-eye', 'glasses', 'nose', 'mouth', 'upper-lip', 'lower-lip']
TempFrameFormat = Literal['jpg', 'png', 'bmp']
OutputAudioEncoder = Literal['aac', 'libmp3lame', 'libopus', 'libvorbis']
OutputVideoEncoder = Literal['libx264', 'libx265', 'libvpx-vp9', 'h264_nvenc', 'hevc_nvenc', 'h264_amf', 'hevc_amf']
OutputVideoPreset = Literal['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow']

ModelValue = Dict[str, Any]
ModelSet = Dict[str, ModelValue]
OptionsWithModel = TypedDict('OptionsWithModel',
{
	'model' : ModelValue
})

ExecutionProviderKey = Literal['cpu', 'coreml', 'cuda', 'directml', 'openvino', 'rocm', 'tensorrt']
ExecutionProviderValue = Literal['CPUExecutionProvider', 'CoreMLExecutionProvider', 'CUDAExecutionProvider', 'DmlExecutionProvider', 'OpenVINOExecutionProvider', 'ROCMExecutionProvider', 'TensorrtExecutionProvider']
ExecutionProviderSet = Dict[ExecutionProviderKey, ExecutionProviderValue]
ValueAndUnit = TypedDict('ValueAndUnit',
{
	'value' : str,
	'unit' : str
})
ExecutionDeviceFramework = TypedDict('ExecutionDeviceFramework',
{
	'name' : str,
	'version' : str
})
ExecutionDeviceProduct = TypedDict('ExecutionDeviceProduct',
{
	'vendor' : str,
	'name' : str
})
ExecutionDeviceVideoMemory = TypedDict('ExecutionDeviceVideoMemory',
{
	'total' : ValueAndUnit,
	'free' : ValueAndUnit
})
ExecutionDeviceUtilization = TypedDict('ExecutionDeviceUtilization',
{
	'gpu' : ValueAndUnit,
	'memory' : ValueAndUnit
})
ExecutionDevice = TypedDict('ExecutionDevice',
{
	'driver_version' : str,
	'framework' : ExecutionDeviceFramework,
	'product' : ExecutionDeviceProduct,
	'video_memory' : ExecutionDeviceVideoMemory,
	'utilization' : ExecutionDeviceUtilization
})

UiWorkflow = Literal['instant_runner', 'job_runner', 'job_manager']

JobStore = TypedDict('JobStore',
{
	'job_keys' : List[str],
	'step_keys' : List[str]
})
JobOutputSet = Dict[str, List[str]]
JobStatus = Literal['drafted', 'queued', 'completed', 'failed']
JobStepStatus = Literal['drafted', 'queued', 'started', 'completed', 'failed']
JobStep = TypedDict('JobStep',
{
	'args' : Args,
	'status' : JobStepStatus
})
Job = TypedDict('Job',
{
	'version' : str,
	'date_created' : str,
	'date_updated' : Optional[str],
	'steps' : List[JobStep]
})
JobSet = Dict[str, Job]

StateContext = Literal['core', 'uis']
StateKey = Literal\
[
	'config_path',
	'source_paths',
	'target_path',
	'output_path',
	'jobs_path',
	'force_download',
	'skip_download',
	'headless',
	'log_level',
	'execution_device_id',
	'execution_providers',
	'execution_thread_count',
	'execution_queue_count',
	'video_memory_strategy',
	'system_memory_limit',
	'face_detector_model',
	'face_detector_size',
	'face_detector_angles',
	'face_detector_score',
	'face_landmarker_score',
	'face_recognizer_model',
	'face_selector_mode',
	'face_selector_order',
	'face_selector_age',
	'face_selector_gender',
	'reference_face_position',
	'reference_face_distance',
	'reference_frame_number',
	'face_mask_types',
	'face_mask_blur',
	'face_mask_padding',
	'face_mask_regions',
	'trim_frame_start',
	'trim_frame_end',
	'temp_frame_format',
	'keep_temp',
	'output_image_quality',
	'output_image_resolution',
	'output_audio_encoder',
	'output_video_encoder',
	'output_video_preset',
	'output_video_quality',
	'output_video_resolution',
	'output_video_fps',
	'skip_audio',
	'frame_processors',
	'open_browser',
	'ui_layouts',
	'ui_workflow'
]
State = TypedDict('State',
{
	'config_path' : str,
	'source_paths' : List[str],
	'target_path' : str,
	'output_path' : str,
	'jobs_path' : str,
	'force_download' : bool,
	'skip_download' : bool,
	'headless' : bool,
	'log_level': LogLevel,
	'execution_device_id' : str,
	'execution_providers' : List[ExecutionProviderKey],
	'execution_thread_count' : int,
	'execution_queue_count' : int,
	'video_memory_strategy' : VideoMemoryStrategy,
	'system_memory_limit' : int,
	'face_detector_model' : FaceDetectorModel,
	'face_detector_size' : str,
	'face_detector_angles' : List[Angle],
	'face_detector_score' : Score,
	'face_landmarker_score' : Score,
	'face_recognizer_model' : FaceRecognizerModel,
	'face_selector_mode' : FaceSelectorMode,
	'face_selector_order' : FaceSelectorOrder,
	'face_selector_age' : FaceSelectorAge,
	'face_selector_gender' : FaceSelectorGender,
	'reference_face_position' : int,
	'reference_face_distance' : float,
	'reference_frame_number' : int,
	'face_mask_types' : List[FaceMaskType],
	'face_mask_blur' : float,
	'face_mask_padding' : Padding,
	'face_mask_regions' : List[FaceMaskRegion],
	'trim_frame_start' : int,
	'trim_frame_end' : int,
	'temp_frame_format' : TempFrameFormat,
	'keep_temp' : bool,
	'output_image_quality' : int,
	'output_image_resolution' : str,
	'output_audio_encoder' : OutputAudioEncoder,
	'output_video_encoder' : OutputVideoEncoder,
	'output_video_preset' : OutputVideoPreset,
	'output_video_quality' : int,
	'output_video_resolution' : str,
	'output_video_fps' : float,
	'skip_audio' : bool,
	'frame_processors' : List[str],
	'open_browser' : bool,
	'ui_layouts' : List[str],
	'ui_workflow' : UiWorkflow
})
StateSet = Dict[StateContext, State]
