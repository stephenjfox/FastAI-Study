https://forums.fast.ai/t/truncated-notebooks/24533/7?u=stephenjfox
* A saint from the Fast.AI forums, who's gone ahead and debugged the system
  configuration with Paperspace, saving me the pain and heartache.

The reason I failed with GCP was
1. Not enough storage on my instance
2. Using a sub-project has permissions that are set that I don't understand,
  because the rules have changed in the last 2 months __significantly__

[2018년 12월 13일]

[오전 6시 42분]

Struggle bus has finally pulled out of the station.
* I've got __two__ different VMs (one in Paperspace, one in GCP) running my crap
  + The trick: `jupyter notebook --ip='0.0.0.0'`
    - Without this, it will start the app on an ip that it doesn't own, but will
      convince the internal networking that it's correct
  * The GCP instance has a little more overhead because
    - Start-up scripts aren't running to completion (for some reason)
    - The Fast.ai scripts aren't run, so I have to manually pull the data.
