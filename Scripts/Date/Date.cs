using UnityEngine;
using UnityEngine.UI;
using System;
using TMPro;

public class Date : MonoBehaviour
{
    // References
    public TMP_Text time; // If you aren't using Text Mesh Pro then replace "TMP_Text" with "Text"

    //Update
    void Update()
    {
        string time = System.DateTime.UtcNow.ToLocalTime().ToString("M/d/yyyy  hh:mm:ss tt");
        time.text = time;
    }
}
