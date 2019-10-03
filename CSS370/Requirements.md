Sample requirements for projects

# Shopping Mall Navigation App

## Major components
  - precision location service
  - text to speech
  - local caching

## Requirements
- App must retrieve data of the nearest bulding(s)
- App must authenticate location usage
- App must narrow down user's location (to the nearest meter(?))
- App must wait for user to select a target location
- App must show info of target location
- App must dynamically generate a direction set using the shortest path
- App must give a visual representation of directions
  - Directions may be given as a standard map view
  - Directions may be given as an augmented reality view
- App must speak directions at user's desires
- App must have text based directions at user's desires

# Sign Language to Speech App

## Major Componenents
  - computer vision
  - visual media (video)
  - text to speech

## Requirements
- App must retrive latest lingustic data from an external database
- App must be able to authenticate use of the camera
- Once authenticated, the app must take the camera's video feed and gather data
- The app must wait for hands to appear in view.
- The app must find the hands position and converts it to a best guess grammar
- The app must be able to distinguish "dialect".
- The app must speak whatever text was generated.
