using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class UrlOpener : MonoBehaviour
{
    public string Url; // you would put in your url in unity
    public void OpenURL()
    {
        Application.OpenURL(Url); 
        Debug.Log("URL Opened!!!"); 
    }
}