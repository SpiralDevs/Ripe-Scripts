using UnityEngine;
using Photon.Pun;
using UnityEngine.SceneManager;

public class NoInternet : MonoBehaviour
{


     if(Application.internetReachability == NetworkReachability.NotReachable)
        {
            Debug.Log("Error. Check internet connection!");
        }
}