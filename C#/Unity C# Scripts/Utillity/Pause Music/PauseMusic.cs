using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PauseMusic : MonoBehaviour
{
    // References
    [SerializeField] private AudioSource m_Music;
    private bool musicIsPaused

    // Start
    void Start()
    {
        m_Music = GetComponent<AudioSource>();
    }

    void Update()
    {
        SetMusic();
    }

    public void Pause()
    {
        musicIsPaused = true;
    }

    public void UnPause()
    {
        musicIsPaused = false;
    }

    public void SetMusic()
    {
        if (musicIsPaused == true)
        {
            m_Music.Pause();
        }
        else
        {
            m_Music.UnPause();
        }
    }
}